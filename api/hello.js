const { spawn } = require('child_process');
const path = require('path');

exports.handler = async function(event, context) {
  // Only allow GET requests
  if (event.httpMethod !== 'GET') {
    return {
      statusCode: 405,
      body: 'Method Not Allowed',
    };
  }

  return {
    statusCode: 200,
    body: JSON.stringify({ message: 'Hello from Netlify Function!' }),
  };
};
