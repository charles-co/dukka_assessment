import { createStore } from 'vuex'

const store = createStore({
    state: {
        isLoggedin: false
    },
    mutations: {
        setUserLoginStatus(state, isLoggedin) {
            console.log("here in sstate")
            state.isLoggedin = isLoggedin
        }
    }
})

export default store
