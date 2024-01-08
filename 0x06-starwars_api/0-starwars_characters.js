#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Invalid HTTP response code:', response.statusCode);
    process.exit(1);
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  characters.forEach((characterUrl) => {
    request(characterUrl, (characterError, characterResponse, characterBody) => {
      if (characterError) {
        console.error('Error:', characterError);
        process.exit(1);
      }

      if (characterResponse.statusCode !== 200) {
        console.error('Invalid HTTP response code:', characterResponse.statusCode);
        process.exit(1);
      }

      const character = JSON.parse(characterBody);
      console.log(character.name);
    });
  });
});
