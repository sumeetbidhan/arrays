# Define a class for DVD
class DVD:
  def __init__(self, name, release_year, director):
    self.name = name
    self.release_year = release_year
    self.director = director

  
  def __str__(self):
    return f"{self.name}, directed by {self.director}, released in {self.release_year}"

# Create a list to hold up to 15 DVDs
dvd_collection = [None] * 15

# Example of adding a DVD to the collection
dvd_collection[0] = DVD("Inception", 2010, "Christopher Nolan")

# Print the details of the first DVD in the collection
print(dvd_collection)

print(len(dvd_collection))