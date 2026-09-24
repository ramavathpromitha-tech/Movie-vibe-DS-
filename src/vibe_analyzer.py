"""
Movie Vibe Analyzer & Recommendation System
A starter module for analyzing movie vibes and recommending movies based on mood.
"""

def analyze_vibe(movie_title: str, genres: list[str], mood_keywords: list[str]) -> dict:
    """
    Classifies a movie's vibe based on genres and mood keywords.
    """
    vibe_mapping = {
        "cozy": ["Animation", "Family", "Comedy", "Romance"],
        "thrilling": ["Action", "Thriller", "Crime", "Mystery"],
        "mind-bending": ["Sci-Fi", "Mystery", "Psychological"],
        "tearjerker": ["Drama", "Romance"],
        "feel-good": ["Comedy", "Adventure", "Music"]
    }
    
    matched_vibes = []
    for vibe, tags in vibe_mapping.items():
        if any(tag in genres for tag in tags):
            matched_vibes.append(vibe)
            
    return {
        "movie": movie_title,
        "genres": genres,
        "primary_vibe": matched_vibes[0] if matched_vibes else "neutral",
        "all_vibes": matched_vibes
    }

if __name__ == "__main__":
    example = analyze_vibe("Inception", ["Sci-Fi", "Action"], ["dreams", "reality"])
    print(f"Sample Analysis: {example}")
