const getStart = document.getElementById("getStart");
const inputSec = document.getElementById("inputSec");
const hero = document.getElementById("hero");

const articleInput = document.getElementById("articleInput");
const analyzeBtn = document.getElementById("analyzeBtn");

const resultSection = document.getElementById("resultSection");
const summaryOutput = document.getElementById("summaryOutput");
const sentimentOutput = document.getElementById("sentimentOutput");
const keywordsOutput = document.getElementById("keywordsOutput");
const entitiesOutput = document.getElementById("entitiesOutput");


const qaSection = document.getElementById("qaSection");
const askBtn = document.getElementById("askBtn");
const questionInput = document.getElementById("questionInput");
const answerOutput = document.getElementById("answerOutput");

getStart.addEventListener("click", function () {
  inputSec.style.display = "block";
  hero.style.display = "none";
});


analyzeBtn.addEventListener("click", function(){
  const userArticle = articleInput.value;

  if (userArticle === "") {
    alert("Please provide an article.");
    return;
  }

  analyzeBtn.disabled = true;
  analyzeBtn.textContent = "Analyzing...";

  fetch("/analyze", {
    method: "POST",
    headers: {
      "Content-type": "application/json",
    },
    body: JSON.stringify({
      article: userArticle,
    }),
  })
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    summaryOutput.textContent = data.summary;
    sentimentOutput.textContent = data.sentiment;
    keywordsOutput.innerHTML = data.keywords.join(", ");
    entitiesOutput.innerHTML = "";

    data.entities.forEach((entity) => {
      entitiesOutput.innerHTML += `<p>${entity.text} (${entity.label})</p>`;
    });

    resultSection.style.display = "block";
    inputSec.style.display = "none";
    qaSection.style.display = "block";
  })

  .catch(function (error) {
    console.error(error);
    alert("Something went wrong.");

    analyzeBtn.disabled = false;
    analyzeBtn.textContent = "Analyze";
  });
    

    

});

askBtn.addEventListener("click",function(){
  const userq = questionInput.value;
  const userArticle = articleInput.value;
  

  if (userq === "") {
    alert("Please ask a question");
    return;
  }
  askBtn.disabled = true;  
  askBtn.textContent = "Answering..."

  fetch("/ask", {
    method: "POST",
    headers: {
      "Content-type": "application/json",
    },
    body: JSON.stringify({
      question: userq,
      article: userArticle,
    }),
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      answerOutput.textContent = data.content;
      askBtn.disabled = false;
      askBtn.textContent = "Ask";
    })
  .catch(function (error) {
    console.error(error);
    alert("Something went wrong.");

    askBtn.disabled = false;
    askBtn.textContent = "Ask";
  });


});
