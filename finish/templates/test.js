

const options = {
    method: 'GET',
    headers: { 'Accept': 'application/json', 'X-API-Key': 'qoTYAokKqHK6xS5e0Zbq3qg2kh2uUzy4FfObczDjE5VdBa9Pi87PDxRl3RV54Fpc' },
  };
  fetch('https://deep-index.moralis.io/api/v2/block/1000?chain=eth', options)
    .then((response) => response.json())
    .then((response) => printResult(response))
    .catch((err) => console.error(err))
  
  const printResult = (response) => {
    const container = document.getElementById('result')
    container.innerHTML = "<pre>" + JSON.stringify(response ,null, 2) + "</pre>"
  }