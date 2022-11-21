const Koa = require('koa')
const bodyParser = require('koa-bodyparser')()
const cors = require('koa2-cors')

const publicRouter = require('./router/index')
const errorHandler = require('./middleware/errorHandler')

const app = new Koa()

app.use(cors({
    credentials: true
}))

// Error Handler
app.use(errorHandler)

// Global Middlewares
app.use(bodyParser)

// Routes
app.use(publicRouter.routes(), publicRouter.allowedMethods())

module.exports = app
