#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  const filmId = process.argv[2];
  request(`${API_URL}/films/${filmId}/`, (err, res, body) => {
    if (err) {
      return console.error('Error:', err);
    }

    try {
      const charactersURL = JSON.parse(body).characters;
      const characterPromises = charactersURL.map(
        url => new Promise((resolve, reject) => {
          request(url, (promiseErr, __, charactersReqBody) => {
            if (promiseErr) {
              return reject(promiseErr);
            }
            try {
              resolve(JSON.parse(charactersReqBody).name);
            } catch (parseErr) {
              reject(parseErr);
            }
          });
        })
      );

      Promise.all(characterPromises)
        .then(names => console.log(names.join('\n')))
        .catch(allErr => console.error('Error:', allErr));
    } catch (parseErr) {
      console.error('Failed to parse film data:', parseErr);
    }
  });
} else {
  console.error('Usage: ./script.js <film_id>');
}
