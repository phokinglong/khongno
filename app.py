from flask import Flask, render_template, request

app = Flask(__name__)

# Route for Question 1 (Personal Information)
@app.route('/question1', methods=['GET', 'POST'])
def question1():
    if request.method == 'POST':
        # Collect data from the form
        name = request.form.get('name')
        birthday = request.form.get('birthday')
        email = request.form.get('email')
        phone = request.form.get('phone')

        # Pass data to Question 2
        return render_template('question2.html', user_data={
            'name': name,
            'birthday': birthday,
            'email': email,
            'phone': phone,
        })
    return render_template('question1.html')

# Route for Question 2 (Income and Assets)
@app.route('/question2', methods=['GET', 'POST'])
def question2():
    if request.method == 'POST':
        # Collect data
        income_sources = request.form.getlist('income_type[]')
        income_amounts = request.form.getlist('income_amount[]')

        # Validate data
        if not income_sources or not income_amounts:
            return render_template('question2.html', error="Please provide income details.")

        # Pass data to the next step
        return render_template('question3.html', income_data={
            'income_sources': income_sources,
            'income_amounts': income_amounts,
        })

    # Render the correct Question 2 template
    return render_template('question2.html')

# Route for Question 3 (Debt Details)
@app.route('/question3', methods=['GET', 'POST'])
def question3():
    if request.method == 'POST':
        try:
            # Collect income data forwarded from Question 2
            income_sources = request.form.getlist('income_type[]')
            income_amounts = request.form.getlist('income_amount[]')

            # Collect debt data for Question 3
            debts = request.form.getlist('debt_amount[]')

            # Validate inputs
            if not debts:
                return render_template(
                    'question3.html',
                    income_data={
                        'income_sources': income_sources,
                        'income_amounts': income_amounts,
                    },
                    error="Please provide debt details."
                )

            # Calculate totals
            total_income = sum(map(float, income_amounts)) if income_amounts else 0
            total_debt = sum(map(float, debts)) if debts else 0

            # Handle zero income edge case
            if total_income == 0:
                status_message = "Income is zero. Please review your financial information."
            else:
                # Calculate debt-to-income ratio
                debt_to_income_ratio = total_debt / total_income
                if debt_to_income_ratio > 1:
                    status_message = "You have a high level of debt. Prioritize repayment."
                elif debt_to_income_ratio > 0.5:
                    status_message = "You have a manageable level of debt."
                else:
                    status_message = "You have a low level of debt. Good job!"

            # Pass results to the completion page
            return render_template('completion.html', result={
                'total_income': total_income,
                'total_debt': total_debt,
                'status_message': status_message,
            })
        except ValueError:
            return render_template(
                'question3.html',
                income_data={
                    'income_sources': income_sources,
                    'income_amounts': income_amounts,
                },
                error="Invalid data provided. Please try again."
            )
        except Exception as e:
            return render_template(
                'question3.html',
                income_data={
                    'income_sources': income_sources,
                    'income_amounts': income_amounts,
                },
                error=f"An error occurred: {str(e)}"
            )

    # Render Question 3 page by default (for GET requests)
    # You need to pass income_data from Question 2 to Question 3
    income_data = request.args.get('income_data', None)
    return render_template('question3.html', income_data=income_data)

@app.route('/completion', methods=['POST'])
def completion():
    if request.method == 'POST':
        # Collect income and debt data
        income_amounts = request.form.getlist('income_amount[]')
        debts = request.form.getlist('debt_amount[]')

        # Convert to float and calculate totals
        total_income = sum(map(float, income_amounts))
        total_debt = sum(map(float, debts))

        # Analyze financial status
        debt_to_income_ratio = total_debt / total_income if total_income > 0 else 0
        status_message = "Unknown"
        if debt_to_income_ratio > 1:
            status_message = "You have a high level of debt. Prioritize repayment."
        elif debt_to_income_ratio > 0.5:
            status_message = "You have a manageable level of debt."
        else:
            status_message = "You have a low level of debt. Good job!"

        # Pass results to the completion page
        return render_template('completion.html', result={
            'total_income': total_income,
            'total_debt': total_debt,
            'status_message': status_message,
        })

    # For GET requests or invalid access
    return "Invalid Access", 404

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
