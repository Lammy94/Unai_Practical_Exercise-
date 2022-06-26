#!/usr/bin/env python3

from requests import get

class Cocktails:
    api_key = 1
    db_endpoint = "https://www.thecocktaildb.com/api/json/v1/"

    def __init__(self, as_string):
        # Make variable part of the object, as a list
        self.ingredients = as_string.split(",")

        # Use the single ingredient endpoint to get list of drinks
        self.options = self.single_ingredient()

    def single_ingredient(self):
        """
        This function is the free version, loops through all ingredients, then
        clears duplicates
        """
        # Create a list to hold all values
        all_options = []

        # Loop over each ingredient
        for each in self.ingredients:
            # Construct the url and make the get request
            response = get(
                f"{self.db_endpoint}/{self.api_key}/filter.php?i={each}"
            )

            # Add any discovered cocktails to the list
            all_options.extend(response.json()['drinks'])

        # Get only the names of each drink
        all_options = [this['strDrink'] for this in all_options]

        # Remove any duplicates found during search
        all_options = list(dict.fromkeys(all_options))

        # Return the value
        return all_options

    def multi_ingredient_api(self):
        """
        This function uses the premium endpoint to run the search, unsure
        whether paying for an API key was outside of scope for the task.
        added the function for good measure; although not called, it would be
        trivial to make code run this instead of single ingredient version
        """
        # Turn the List back into a comma separated string
        list_as_string = self.ingredients.join(",")

        # Make the get request
        response = get(
            f"{self.db_endpoint}/{self.api_key}/filter.php?i={list_as_string}"
        )

        # Return the value
        return response.json()['drinks']


def get_ingredients():
    """
    Function to deal with the input from the user
    """
    # Replace makes sure no spaces were seen in string
    input_values = input(
        "Please input the ingredients you'd like to use.\n"
        "Separate each with a comma & use underscores instead of spaces in "
        "ingredient names\n"
        "e.g. Dry_Vermouth,Gin,Anis"
    )

    # Make sure there were no spaces in the input string
    input_values = input_values.replace(" ", "")

    return input_values


if __name__ == '__main__':
    ingredients = get_ingredients()
    search = Cocktails(ingredients)

    print(f"{len(search.options)} results found")
    print("\nBased on whats in you cupboard,\n"
          "some drinks you could make are:")

    for option in search.options:
        print(option)
