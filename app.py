from flask import Flask, request, render_template
import pandas as pd

# Load your data
jee = pd.read_csv("Data/data.csv")
jee.drop(jee[jee['institute_type'] == 'IIT'].index, inplace=True)

app = Flask(__name__)

def college_predictor(rank, caste, state, genders, homestate):
    results = []  # List to store matching rows
    for index, row in jee.iterrows():
        opening_rank = row['opening_rank']
        closing_rank = row['closing_rank']
        quota = row['quota']
        category = row['category']
        pool = row['pool']
        institute_short = row['institute_short']

        # Check if the rank is within the opening and closing ranks
        if opening_rank <= rank <= closing_rank or opening_rank >= rank:
            # Check if the caste matches
            if caste == category:
                # Check if state matches quota
                if state == quota or institute_short == homestate:
                    # Check if gender matches
                    if genders in [pool, 'Gender-Neutral']:
                        results.append(row.to_dict())  # Append the entire row as a dictionary

    # Remove duplicates by converting to DataFrame and using drop_duplicates
    results_df = pd.DataFrame(results)
    results_df.drop_duplicates(inplace=True)
    unique_results = results_df.to_dict(orient='records')  # Convert back to list of dicts

    return unique_results  # Return the list of unique rows that match the criteria

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            rank = int(request.form['rank'])
            caste = request.form['caste']
            state = request.form['state']
            genders = request.form['genders']
            homestate = request.form['homestate']

            # Call the college_predictor function
            data = college_predictor(rank, caste, state, genders, homestate)

            # Render results to a new HTML page
            return render_template('results.html', results=data)
        except ValueError:
            return "May be there is no sutaible colleges for this rank in my search engine ", 400  # Return an error for invalid input

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
