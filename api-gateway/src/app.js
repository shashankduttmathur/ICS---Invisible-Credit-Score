
require('dotenv').config();
const express = require('express');
const helmet = require('helmet');
const morgan = require('morgan');
const routes = require('./routes');

const app = express();
app.use(express.json());
app.use(helmet());
app.use(morgan('dev'));

app.use('/api', routes);

app.listen(3000, () => console.log('API running on 3000'));
