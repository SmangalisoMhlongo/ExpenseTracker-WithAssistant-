from data_manager import get_all_expenses

#creating a simple rule bvased NLP as the "AI" assistant 
def ask_ai(question):
    q = question.lower()
    df = get_all_expenses()

    if "total" in q and "spend" in q:
        total = df["amount"].sum()
        return f"You spent a total of R{total:.2f}."

    if "highest" in q or "most" in q:
        if df.empty:
            return "No expenses yet."
        cat = df.groupby("category")["amount"].sum().idxmax()
        return f"Your highest spending category is {cat}."

    if "breakdown" in q or "categories" in q:
        if df.empty:
            return "No expenses yet."
        breakdown = df.groupby("category")["amount"].sum()
        breakdown_str = "\n".join([f"{cat}: R{amt:.2f}" for cat, amt in breakdown.items()])
        return f"Spending by category:\n{breakdown_str}"

    return "I'm not sure how to answer that. Try asking about totals or categories." 