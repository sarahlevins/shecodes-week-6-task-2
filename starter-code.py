class Item():

    def __init__(self, name, barcode):
        self.name = name
        self.barcode = barcode
        self.is_valid = False

    def __str__(self):
        # You will need to override this method to print the item name and whether the barcode
        # is valid or invalid, with sensible formatting.
        pass


    def main(shopping_list, credit_card_number):
        '''Outputs a summary of whether each item's barcode is valid or invalid.

        Args:
          shopping_list (list): A list of dictinaries, where each dictionary is a shopping item of the following format:
            {
              'item': 'Bread',
              'barcode': '9400550619775',
              'type': 'grocery-item'
            },
            Where the type could be: grocery-item, isbn10-book or isbn13-book
          credit_card_number (string): A credit card number.
         
        Returns:
          (string): A summary of whether each item and the credit card is valid or invalid.
        '''
        pass


if __name__ == '__main__':
  # This is example input to get you started
  # These are all valid barcodes
    shopping_list = [
        {
            'item': 'Bread',
            'barcode': '9400550619775',
            'type': 'grocery-item'
        },
        {
            'item': 'Milk',
            'barcode': '9400550619775',
            'type': 'grocery-item'
        },
        {
            'item': 'Orange Juice',
            'barcode': '9400550619775',
            'type': 'grocery-item'
        },
        {
            'item': 'The Very Hungry Caterpillar',
            'barcode': '0306406152',
            'type': 'isbn10-book'
        }
    ]
    credit_card_number = 4012000033330026 # Valid
    main(shopping_list, credit_card_number)
  
    # You will need to print the resulting summary
