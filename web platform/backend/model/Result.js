const {
    CODE_ERROR,
    CODE_SUCCESS
} = require('../utils/constant')

class Result {
    constructor(data, msg = 'Operate successful', options) {
        this.data = null
        if (arguments.length === 0) {
            this.msg = 'Operate successful'
        } else if (arguments.length === 1) {
            this.msg = data
        } else {
            this.data = data
            this.msg = msg
            if (options) {
                this.options = options
            }
        }
    }

    createResult() {
        if (!this.code) {
            this.code = CODE_SUCCESS
        }
        let base = {
            code: this.code,
            msg: this.msg
        }
        if (this.data) {
            base.data = this.data
        }
        if (this.options) {
            base = { ...base, ...this.options }
        }
        console.log(base)
        return base
    }

    json(ctx, options=null) {
        ctx.body = this.createResult()
        if (options) {
            ctx.status = options.status
        }
    }

    success(ctx) {
        this.code = CODE_SUCCESS
        this.json(ctx)
    }

    fail(ctx) {
        this.code = CODE_ERROR
        this.json(ctx)
    }
}

module.exports = Result
