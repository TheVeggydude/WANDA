from django.core.management.base import BaseCommand, CommandError
from viewer import utils
from viewer.models import *

class Command(BaseCommand):
    help = 'Loads a standard file (data.json), from the top level \'data\' directory, into the database.'
    
    
    # Removes all previous data from the database
    def _remove_data(self):
        Answer.objects.all().delete()
        Node.objects.all().delete()
        Tree.objects.all().delete()
    
    
    # Creates all the data by reading from a hard coded location
    def _create_data(self):
        
        # Creates a dictionary that needs to be translated to a set of objects
        tree = utils.read_tree_from_file('../data/data.json')
        
        # Recursively create Question objects from the dictionary
        
    
    # Main command handler - denotes the sub-steps taken
    def handle(self, *args, **options):
        self._remove_data()
        self._create_data()