
const router = require('express').Router();
const score = require('../controllers/scoreController');

router.post('/score', score.getScore);

module.exports = router;
