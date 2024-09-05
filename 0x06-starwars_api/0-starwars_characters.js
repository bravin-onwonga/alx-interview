#!/usr/bin/node
const request = require('request');

const film = process.argv;

if (film.length < 3) {
  console.log('Usage: ./0-starwars_characters.js <film number>');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${film[2]}/`;

request(url, (err, res, body) => {
  if (err) console.log(err);

  body = JSON.parse(body);

  const characterUrls = body.characters;

  for (const characterUrl of characterUrls) {
    request(characterUrl, (err, res, body) => {
      if (err) console.log(err);

      body = JSON.parse(body);

      console.log(body.name);
    });
  }
});
