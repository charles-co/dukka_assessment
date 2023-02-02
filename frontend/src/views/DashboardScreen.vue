<template>

    <div class="container my-5">
        <button class="btn btn-outline-primary btn-lg" @click="greet" v-if="!show">Click Me</button>
        <Transition>
            <div v-if="show" class="alert alert-primary animate__animated animate__fadeIn" role="alert">
                <h4 class="alert-heading">Hi {{ user.name }},</h4>
                <p>Welcome to your dashboard</p>
                <hr>
                <p class="mb-0">I hope you enjoyed our simple simulation of speech to text. Bye for now</p>
            </div>
        </Transition>
    </div>

</template>

<script>
import axiosInstance from '@/axios';

export default {

    name: 'DashboardScreen',
    data() {
        return {
            message: "",
            user: null,
            synth: window.speechSynthesis,
            voiceList: [],
            show: false,
            greetingSpeech: new window.SpeechSynthesisUtterance()
        }
    },
    mounted() {
        this.getUserDetails();
    },
    methods: {
        getUserDetails() {
            axiosInstance.get("/api/v1/users")
                .then(response => {
                    if (response.status === 200) {
                        this.user = response.data;
                        this.message = `Hi ${this.user.name}, Welcome to your dashboard. I hope you enjoyed our simple simulation of speech to text. Bye for now`;
                        this.voiceList = this.synth.getVoices();
                    }
                })
                .catch(error => {
                    console.log(error);
                });
        },
        greet() {
            this.greetingSpeech.text = this.message;
            this.greetingSpeech.voice = this.voiceList[140];
            this.show = true;
            this.synth.speak(this.greetingSpeech);
        }
    }
}
</script>
