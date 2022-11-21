const {CODE_ERROR} = require('../utils/constant')

const errorHandler = (ctx, next) => {
    return next().catch(err => {
        if (err.code == null) {
            console.log(err.stack)
        }
        ctx.body = {
            code: err.code || CODE_ERROR,
            data: null,
            msg: err.message.trim()
        }
        // 保证返回状态是 200
        ctx.status = 200
        return Promise.resolve()
    })
}

module.exports = errorHandler
