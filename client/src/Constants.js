// Constants.js
const production = {
    url: '' // Replace with your production URL
  };
  const development = {
    url: 'http://127.0.0.1:5000' // Use your Flask development server URL
  };
  export const config = process.env.NODE_ENV === 'development' ? development : production;