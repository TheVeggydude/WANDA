from django.core.management.base import BaseCommand, CommandError
from viewer import utils
from viewer.models import *

class Command(BaseCommand):
    help = 'Loads a standard file (data.json), from the top level \'data\' directory, into the database.'
    
    
    # Removes all previous data from the database
    def _remove_data(self):
        Answer.objects.all().delete()
        Question.objects.all().delete()
        Tree.objects.all().delete()
    
    
    # Recursively transforms nodes in the dictionary to a Question object for in the tree
    def json_to_node(self, dict):
        
        #TODO This is sort of a hack in my opinion... Reconsider the whole node/question model thing?
        # If you are looking at an end node in stead of a normal question only add question text
        if 'End' in dict:
            leaf, created = Question.objects.get_or_create(text = dict['End'])
            if created:
                # Initial save to create object in database
                leaf.save()
            return leaf
        
        # Try to find an existing question object with the same question, or create a new one if it doesn't exist yet
        question, created = Question.objects.get_or_create(text = dict['Question'])
        
        # It is was already created we need not do anything but return the object so we can have
        # Multiple questions referring to the same question
        if created:
            # Initial save to create object in database
            question.save()
            
            # Create Answer objects for all the answers and add them to the question object
            # At the same time recursively get a new question object related to that answer
            for answer_dict in dict['Answers']:

                answer = Answer(text= answer_dict['Text'], question = question)
                answer.save()

                child_question = self.json_to_node(answer_dict['Node'])
                question.children.add(child_question)
            
            # Save again as there have been (numeral) changes
            question.save()
                
        return question
    
    
    # Creates all the data by reading from a hard coded location
    def _create_data(self):
        
        # Creates a dictionary that needs to be translated to a set of objects
        dict = utils.read_tree_from_file('../data/data.json')
        
        # Recursively create Question objects from the dictionary
        tree = Tree(start = self.json_to_node(dict['Tree']))
        tree.save()
    
    
    # Main command handler - denotes the sub-steps taken
    def handle(self, *args, **options):
        self._remove_data()
        self._create_data()