function submitQuiz() {
    const form = document.getElementById("quiz-form");
    const formData = new FormData(form);

    // Convert form data to JSON
    const answers = {};
    formData.forEach((value, key) => {
        answers[key] = value;
    });

    // Send data to the Flask backend
    fetch('/evaluate-quiz', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(answers)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("quiz-result").innerHTML = 
            `<p>Your Score: ${data.score}/${data.total}</p>`;
    });
}
