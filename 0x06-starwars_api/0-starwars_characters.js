#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const requestURL = 'https://swapi-api.alx-tools.com/api/films';

const fetchCharacterName = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      try {
        const data = JSON.parse(body);
        resolve(data.name);
      } catch (err) {
        console.log(err);
      }
    });
  });
};

request(requestURL, async (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  body = JSON.parse(body);
  const filmData = body.results[filmId - 1];

  const characterPromises = filmData.characters.map(characterURL => {
    let id = characterURL[characterURL.length - 2];

    if (characterURL[characterURL.length - 3] !== '/') {
      id = `${characterURL[characterURL.length - 3]}${id}`;
    }
    const nameURL = `https://swapi-api.alx-tools.com/api/people/${id}/`;
    return fetchCharacterName(nameURL);
  });

  const names = await Promise.all(characterPromises);
  names.forEach((name) => console.log(name));
});
