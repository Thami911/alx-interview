#!/usr/bin/node

const request = require('request');

const MovieID = process.argv[2];
const FilmEndPoint = 'https://swapi-api.hbtn.io/api/films/' + MovieID;
let people = [];
const names = [];

const requestCharacters = async () => {
  await new Promise(resolve => request(FilmEndPoint, (err, res, body) => {
    if (err || res.statusCode !== 200) {
      console.error('Error: ', err, '| StatusCode: ', res.statusCode);
    } else {
      const jsonBody = JSON.parse(body);
      people = jsonBody.characters;
      resolve();
    }
  }));
};

const requestNames = async () => {
  if (people.length > 0) {
    for (const y of people) {
      await new Promise(resolve => request(y, (err, res, body) => {
        if (err || res.statusCode !== 200) {
          console.error('Error: ', err, '| StatusCode: ', res.statusCode);
        } else {
          const jsonBody = JSON.parse(body);
          names.push(jsonBody.name);
          resolve();
        }
      }));
    }
  } else {
    console.error('Error: Got no Characters for some reason');
  }
};

const getCharNames = async () => {
  await requestCharacters();
  await requestNames();

  for (const x of names) {
    if (x === names[names.length - 1]) {
      process.stdout.write(x);
    } else {
      process.stdout.write(x + '\n');
    }
  }
};

getCharNames();