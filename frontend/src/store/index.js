import { createStore } from 'vuex'

const store = createStore({
    state: {
        isLoggedin: false
    },
    mutations: {
        setUserLoginStatus(state, isLoggedin) {
            state.isLoggedin = isLoggedin
        }
    }
})

export default store
