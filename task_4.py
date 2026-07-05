def run_quiz():
    
    quiz_data = {
        "What is the capital of France?": "paris",
        "Which programming language is known for its readability and snake mascot?": "python",
        "How many elements are there in the periodic table? (Enter the number)": "118"
    }
    
    score = 0
    total_questions = len(quiz_data)
    
    print("=" * 50)
    print("Welcome to the General Knowledge Quiz!".center(50))
    print("=" * 50)
    print("Type your answer and press Enter. (Answers are case-insensitive)\n")
    
    
    for question, correct_answer in quiz_data.items():
        print(f"Question: {question}")
        
        
        user_answer = input("Your Answer: ").strip().lower()
        
        
        if user_answer == correct_answer:
            print("✅ Correct!\n")
            score += 1
        else:
            
            print(f"❌ Incorrect. (The correct answer was: {correct_answer.capitalize()})\n")
            
        print("-" * 30)
    
    
    print("\n" + "=" * 50)
    print("QUIZ COMPLETED".center(50))
    print("=" * 50)
    print(f"Your Final Score: {score} / {total_questions}")
    
    
    percentage = (score / total_questions) * 100
    print(f"Performance: {percentage:.1f}%")
    
    
    if score == total_questions:
        print("🏆 Perfect score! Exceptional job!")
    elif score >= total_questions / 2:
        print("👍 Good effort! You passed.")
    else:
        print("📚 Better luck next time! Keep learning.")
    print("=" * 50)


if __name__ == "__main__":
    run_quiz()