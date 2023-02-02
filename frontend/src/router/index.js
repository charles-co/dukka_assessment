// import Vue from 'vue'
import { createRouter, createWebHashHistory } from 'vue-router'
import HomeScreen from '../views/HomeScreen.vue'
import LoginScreen from '../views/LoginScreen.vue'
import SignupScreen from '../views/SignupScreen.vue'
import DashboardScreen from '../views/DashboardScreen.vue'

const routes = [
    {
        path: '/',
        component: HomeScreen,
        name: 'Home',
    },
    {
        path: '/signup',
        component: SignupScreen
    },
    {
        path: '/login',
        component: LoginScreen
    },
    {
        path: '/dashboard',
        component: DashboardScreen
    }
]

const router = createRouter({
    history: createWebHashHistory("localhost:8000/"),
    routes,
})

export default router
