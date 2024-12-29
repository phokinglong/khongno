// Change header background on scroll
const header = document.getElementById('header');
const logo = document.getElementById('logo');

// Add scroll event listener to toggle header background
window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        header.classList.remove('transparent');
        header.classList.add('solid');
    } else {
        header.classList.remove('solid');
        header.classList.add('transparent');
    }
});

// Add a new income entry
function addIncomeEntry() {
    const incomeSection = document.getElementById('income-section');
    const entryCount = incomeSection.children.length + 1;

    // Create a new income entry dynamically
    const newEntry = document.createElement('div');
    newEntry.classList.add('income-entry');
    newEntry.innerHTML = `
        <label for="income-type-${entryCount}">Income Type:</label>
        <select id="income-type-${entryCount}" name="income_type[]" required>
            <option value="" disabled selected>Select income type</option>
            <option value="salary">Salary</option>
            <option value="business">Business</option>
            <option value="investment">Investment</option>
            <option value="freelance">Freelance</option>
            <option value="other">Other</option>
        </select>

        <label for="income-amount-${entryCount}">Income Amount:</label>
        <input type="number" id="income-amount-${entryCount}" name="income_amount[]" placeholder="Enter amount" required>
    `;
    incomeSection.appendChild(newEntry);
}

// Add a new debt entry
function addDebtEntry() {
    const debtSection = document.getElementById('debt-section');
    const entryCount = debtSection.children.length + 1; // Dynamic entry count

    // Create a new debt entry
    const newEntry = document.createElement('div');
    newEntry.classList.add('debt-entry');
    newEntry.innerHTML = `
        <label for="debt-amount-${entryCount}">Debt Amount:</label>
        <input type="number" id="debt-amount-${entryCount}" name="debt_amount[]" placeholder="Enter debt amount" required>

        <label for="debt-type-${entryCount}">Type of Debt:</label>
        <select id="debt-type-${entryCount}" name="debt_type[]" required>
            <option value="" disabled selected>Select debt type</option>
            <option value="credit_card">Credit Card</option>
            <option value="mortgage">Mortgage</option>
            <option value="personal_loan">Personal Loan</option>
            <option value="student_loan">Student Loan</option>
            <option value="other">Other</option>
        </select>

        <label for="monthly-interest-${entryCount}">Monthly Interest Payment:</label>
        <input type="number" id="monthly-interest-${entryCount}" name="monthly_interest[]" placeholder="Enter interest payment" required>

        <label for="repayment-type-${entryCount}">Repayment Type:</label>
        <select id="repayment-type-${entryCount}" name="repayment_type[]" required>
            <option value="" disabled selected>Select repayment type</option>
            <option value="principal_only">Principal Only</option>
            <option value="principal_plus_interest">Principal + Interest</option>
        </select>
    `;
    debtSection.appendChild(newEntry);
}
