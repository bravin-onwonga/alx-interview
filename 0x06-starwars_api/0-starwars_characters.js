#!/usr/bin/node
const axios = require('axios');

const film = process.argv;

if (film.length < 3) {
  console.log('Usage: ./0-starwars_characters.js <film number>');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${film[2]}/`;

axios.get(url).then((res) => {
  const data = res.data;
  const charactersUrls = data.characters;

  for (const characterUrl of charactersUrls) {
    axios.get(characterUrl).then((res) => {
      console.log(res.data.name);
    }).catch((error) => {
      console.log(error);
    });
  }
}).catch((error) => {
  console.log(error);
});
