from collections import defaultdict
import populateDecisionTable

class decisionTree():
    def __init__(self):
        self.attributes = defaultdict(list)

    def build_decision_tree(self,curr,prev,prev2):
        attribute_table = populateDecisionTable.populate_attribute(self.attributes, curr, prev, prev2)

