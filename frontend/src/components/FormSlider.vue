<template>
    <template v-if="type == 'login'">
        <div>
            <Transition name="fade" enter-active-class="animate__animated animate__fadeInRight"
                leave-active-class="animate__animated animate__fadeOutLeft">
                <div v-if="step === 1">
                    <h3>Email address?</h3>
                </div>
            </Transition>
            <Transition name="fade" enter-active-class="animate__animated animate__fadeInRight"
                leave-active-class="animate__animated animate__fadeOutLeft">
                <div v-if="step === 2">
                    <h3>Your Password?</h3>
                </div>
            </Transition>
        </div>
    </template>
    <template v-if="type == 'signup'">
        <div>
            <div class="animate__animated animate__fadeInUp">
                <h2>Let start with a little introduction</h2>
            </div>
            <Transition name="fade" enter-active-class="animate__animated animate__fadeInRight"
                leave-active-class="animate__animated animate__fadeOutLeft">
                <div v-if="step === 1" class="">
                    <h3>What is you name, or what would you like to be called ?</h3>
                </div>
            </Transition>
            <Transition name="fade" enter-active-class="animate__animated animate__fadeInRight"
                leave-active-class="animate__animated animate__fadeOutLeft">
                <div v-if="step === 2">
                    <h3>Hmmm, Email address?</h3>
                </div>
            </Transition>

            <Transition name="fade" enter-active-class="animate__animated animate__fadeInRight"
                leave-active-class="animate__animated animate__fadeOutLeft">
                <div v-if="step === 3">
                    <h3>Are you a man, woman or you rather not say?</h3>
                </div>
            </Transition>
            <Transition name="fade" enter-active-class="animate__animated animate__fadeInRight"
                leave-active-class="animate__animated animate__fadeOutLeft">
                <div v-if="step === 4">
                    <h3>How can we reach you?</h3>
                    <small>kindly call out digit with extension e.g +234 812 909 3242</small>
                </div>
            </Transition>
            <Transition name="fade" enter-active-class="animate__animated animate__fadeInRight"
                leave-active-class="animate__animated animate__fadeOutLeft">
                <div v-if="step === 5">
                    <h3>What country are you from?</h3>
                </div>
            </Transition>

            <Transition name="fade" enter-active-class="animate__animated animate__fadeInRight"
                leave-active-class="animate__animated animate__fadeOutLeft">
                <div v-if="step === 6">
                    <h3>What password would you like to use?</h3>
                </div>
            </Transition>
            <Transition name="fade" enter-active-class="animate__animated animate__fadeInRight"
                leave-active-class="animate__animated animate__fadeOutLeft">
                <div v-if="step === 7">
                    <h3>Can you say that again?</h3>
                </div>
            </Transition>
        </div>
    </template>
    <p>{{ msg }}</p>
    <template v-if="showtranscript">
        <p class="h3 mt-5">Say "next" {{ value }}otherwise say "repeat question"</p>
    </template>
</template>

<script>
import annyang from 'annyang';

export default {

    name: 'FormSlider',
    props: {
        type: {
            type: String,
            required: true,
            validator(value) {
                return ['login', 'signup'].includes(value);
            },
        },
    },
    emits: ['formSubmitted'],
    data() {
        return {
            step: 0,
            login: {
                email: '',
                password: '',
            },
            signup: {
                name: '',
                email: '',
                sex: '',
                phone_number: '',
                country: '',
                password: '',
                password2: '',
            },
            recognition: null,
            transcript: '',
            showtranscript: false,
            msg: '',
            value: '',
            finished: false,
        };
    },
    methods: {
        nextStep() {
            this.msg = '';
            this.value = '';
            if (this.finished) {
                console.log("emitting")
                this.$emit('formSubmitted', { data: this.$data[this.type] })
                annyang.abort()
            }
            let step = this.step;
            this.step = 0;
            setTimeout(() => {
                this.step = step + 1;
                this.acceptInput();
            }, 500);
        },
        repeat(n = -1) {
            let step = this.step;
            this.step = 0;

            setTimeout(() => {
                this.step = n === -1 ? step : n;
                this.acceptInput();
            }, 500);
            this.$data[this.type][this.getkey()] = "";
        },
        prevStep(n = -1) {
            var step = this.step;
            this.step = 0;
            setTimeout(() => {
                if (n === -1) {
                    this.step = step > 1 ? step - 1 : 1;
                }
                else {
                    var tmp = step - n;
                    this.step = tmp < 1 ? 1 : tmp;
                }
                this.acceptInput()
            }, 1000);
        },
        getkey() {
            let keys = Object.keys(this.$data[this.type]);
            let key = keys[this.step - 1];
            return key;
        },
        acceptInput() {
            annyang.abort();
            const SpeechRecognition =
                window.SpeechRecognition || window.webkitSpeechRecognition;
            this.recognition = new SpeechRecognition();
            // this.recognition.onend = function () {
            //     console.log("recognition ended, restarting");
            //     this.startListening();
            // }.bind(this);
            this.recognition.lang = 'en-US';
            this.recognition.interimResults = false;
            this.recognition.maxAlternatives = 1;
            this.startListening();
        },
        startListening() {

            let key = this.getkey();
            this.recognition.start();
            this.recognition.onresult = event => {
                this.transcript = event.results[0][0].transcript;
                console.log("stopping")
                this.recognition.stop();
                annyang.start();
                if (["next", "continue", "next step", "next question"].some(x => this.transcript.includes(x))) {
                    this.nextStep();
                }
                else if (["go back", "back", "previous", "previous step", "previous question"].some(x => this.transcript.includes(x))) {
                    this.prevStep();
                }
                else {
                    if (key == "email") {
                        this.transcript = this.transcript.replace(/^(.+) at (.+)$/i, "$1@$2").toLowerCase().replaceAll(" ", "");
                        this.value = "to continue with " + this.transcript + ", ";
                    }

                    if (key == "sex") {
                        let pattern = /man|woman/;
                        this.transcript = pattern.exec(this.transcript)[0]
                        this.value = "to continue with " + this.transcript + ", ";
                        if (this.transcript == "man") {
                            this.transcript = "M";
                        } else if (this.transcript == "woman") {
                            this.transcript = "F";
                        }
                        else {
                            this.transcript = "O";
                        }
                    }
                    if (key == "phone_number") {
                        this.transcript = this.transcript.replace(/[^0-9]/g, "");
                        if (this.transcript.charAt(0) !== '+') {
                            this.transcript = '+' + this.transcript;
                        }
                        this.value = "to continue with " + this.transcript + ", ";
                    }

                    if (["name", "country"].some((v) => key.includes(v))) {
                        this.value = "to continue with " + this.transcript + ", ";
                    }

                    if (key.includes("password") === true) {
                        this.transcript = this.transcript.replaceAll(" ", "");
                        if (key == "password2") {
                            if (this.transcript != this.$data[this.type]["password"]) {
                                this.msg = "Passwords do not match";
                                this.repeat(6)

                            } else {
                                this.finished = true;
                            }
                        }
                        this.finished = this.type == "login" ? true : false;
                    }

                    this.$data[this.type][key] = this.transcript;
                    this.showtranscript = true;
                    console.log(this.$data[this.type]);
                    annyang.start();
                }
            }
        },
    },
    mounted() {
        setTimeout(() => {
            this.nextStep();
        }, 500);
        const commands = {
            "next": () => {
                this.showtranscript = false;
                this.nextStep();
            },
            "back": () => {
                this.prevStep();
            },
            "go back :step step": {
                regexp: /go back (\d+) step/,
                callback: (step) => {
                    this.prevStep(step);
                },
            },
            "repeat question": () => {
                this.repeat();
            },
        }

        annyang.addCommands(commands);
        annyang.start();

    },
};
</script>
<style>

</style>
