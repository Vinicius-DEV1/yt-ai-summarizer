def main():
    print("=== YT AI SUMMARIZER ===")

    url = input("Enter Youtube URL: ").strip()


    if not url:
        print("Error: URL cannot be empty.")
        return

    #mock extraction
    print("Fetching video transcript...")
    transcript_mock = "sample text simmulating the video transcript."
    
    #mock summarization
    print("Generating summary with Gemini")
    summary_mock = "### Sample Summary\n -Key point\n-Key point"


    #display the final result
    print("\n" + "=" * 30)
    print("Generated summary:")
    print("="*30)
    print(summary_mock)

if __name__ == "__main__":
    main()