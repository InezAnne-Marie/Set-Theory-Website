

public class Bar extends Entertainment {
	// instance variables
	private String musicGenre;
	private String ambiance;
	private String djName;

	// constructor
	public Bar (String m, String a, String d) {
		super();
		this.musicGenre = m;
		this.ambiance = a;
		this.djName = d;
	}

	// getters
	public String getAmbiance() {return this.ambiance; }
	public String getMusicGenre() {return this.musicGenre; }

	// setters
	public void changeAmbiance(String newAmbiance) {this.ambiance = newAmbiance; }
	public void setMusicGenre(String newGenre) {this.musicGenre = newGenre; }

	// other methods
	public boolean isWithinBudget() {}

	// toString & equals methods
	@Override
	public String toString() {}

	@Override
	public boolean equals() {}
}