//arrays01 actual code for creating an Array to hold DVD's.
DVD[] dvdcollection = new DVD[15];

// A simple definition for a DVD.
public class DVD{

  public String name;
  public int releaseYear;
  public String director;
  

  public DVD(String name, int releaseYear, String director){
    this.name = name;
    this.releaseYear = releaseYear;
    this.director = director;

  }

  public String toString(){
    return this.name + ", directed by" + this.director + ", relased in" + this.releaseYear;
  }
  
}