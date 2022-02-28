import math
from sklearn.ensemble import BaggingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier

def create_model():
    
    return MLPClassifier()


class PredictionManager():
  

    def __init__(self, X, y, targets):
        
        # The index of the current sample
        self.index = 1

        # The result of each prediction , 1 = True, 0 = False
        self.prediction = 0

        # The error_rate list used for display
        self.error_rate_list = list()

        # Booleans for drift and warning detection
        self.drift_occured = False
        self.warning_occuring = False

        # X : data used, y : labels target of the data
        self.X = X
        self.y = y

        # The lists of the data in memory during warnings in order to re learn models in case of drift
        self.training_data_X = list()
        self.training_data_y = list()

        # Creating the machine learning model we will use
        self.model = create_model()

        # Creating the concept drift detector instance
        self.cdd = Concept_Drift_Detector()

        # List with every possible label for the model targets 
        self.targets = targets

        # Count of the number of errors by the model prediction
        self.nb_errors = 0

        # This boolean is set to True if the data size for model learning is high enough - I set that to 30
        self.data_size = False


    # Run_all_steps function, called by our main function: 

    def run_all_steps(self):
        
        while self.index < len(self.X)-1 :

            self.model_train()  
            self.model_predict()    
            self.cdd_step()
            self.check_drift()
            self.check_warning_occuring()
            self.index += 1

        #print(confusion_matrix(self.y,self.predict))

        return self.error_rate_list, self.nb_errors



    ### Run_all_steps loop functions :

    def check_warning_occuring(self):

        if self.warning_occuring or self.data_size:
            self.training_data_X.append(self.X[self.index])
            self.training_data_y.append(self.y[self.index])
        else:
            self.training_data_X = list()
            self.training_data_y = list()


    def check_drift(self):

        if self.drift_occured:
            if len(self.training_data_X)>30 :
                self.model = create_model()
                self.model.partial_fit(self.training_data_X, self.training_data_y, self.targets)
                self.drift_occured = False
                self.data_size = False
            else:
                self.data_size = True
        

    def model_train(self): 

        self.model.partial_fit([self.X[self.index]], [self.y[self.index]], self.targets)


    def model_predict(self):
        
        predict = self.model.predict([self.X[self.index+1]])

        if predict[0] == 1 and self.y[self.index+1] == 1:
            self.prediction = "TP"

        elif predict[0] == 1 and self.y[self.index+1] == 0:
            self.prediction = "FP"
            self.nb_errors += 1

        elif predict[0] == 0 and self.y[self.index+1] == 1:
            self.prediction = "FN"
            self.nb_errors += 1

        elif predict[0] == 0 and self.y[self.index+1] == 0:
            self.prediction = "TN"


    def cdd_step(self):

        self.new_error_rate, self.drift_occured, self.warning_occuring = self.cdd.cd_detection_step(self.prediction)
        self.error_rate_list.append(self.new_error_rate)
        


class Concept_Drift_Detector():

    '''
    Concept Drift Detection first implementation
    '''

    
    def __init__(self):

        # This is the minimum of probability to have a false prediction which is the error_rate
        self.p_min = 1

        # This is the minimum of the standard deviation
        self.s_min = 1

        # This is the index of the current evaluated sample
        self.s_index = 1

        # This is the boolean giving the information about a warning : if it is true, a warning is currently happening
        self.warning_occuring = False

        # The differents measures and their standard deviation are initialized here
        self.measure = None
        self.s_measure = None

        # The count of each type of prediction are initialized here : TP = "true positive", FP = "false positive", TN = "true negative", FN = "false negative"
        self.TP = 1
        self.FP = 1
        self.TN = 1
        self.FN = 1


    ### Cdd functions :

    def check(self):

        # Min check
        if (self.measure + self.s_measure) < (self.p_min +  self.s_min) :
            
            self.p_min = self.measure
            self.s_min = self.s_measure
            self.warning_occuring = False
            self.drift_occured = False
            

        # Check if drift occurs
        elif (self.measure + self.s_measure) > (self.p_min + 3 * self.s_min):

            self.p_min = self.measure
            self.s_min = self.s_measure
            self.nb_errors = 0
            self.size = 0
            self.warning_occuring = False
            self.drift_occured = True


        # Check if warning occurs
        elif (self.measure + self.s_measure) > (self.p_min + 2 * self.s_min):

            self.warning_occuring = True
            self.drift_occured = False


        # When nothing happened and nothing is occuring
        else:

            self.warning_occuring = False
            self.drift_occured = False



    ## This function returns the probability to have error in next prediction = p, the index of the sample (or the index of the beginning of the warning, in case of drift),
    ## and a boolean giving the info if there is drift

    def cd_detection_step(self, value):

        # Increment for each count of predictions
        if(value == "TP"):
            self.TP += 1
        elif(value == "FP"):
            self.FP += 1
        elif(value == "TN"):
            self.TN += 1
        elif(value == "FN"):
            self.FN += 1

        self.s_index += 1

        self.measure = ( 2 * self.TP ) / ( 2 * self.TP + self.FN + self.FP)

        self.s_measure = math.sqrt ( self.measure * (1 - self.measure) / ( self.TP + self.FP + self.TN + self.FN ) )

        #print(self.measure, self.s_measure)

        self.check()


        return  self.measure , self.drift_occured, self.warning_occuring
