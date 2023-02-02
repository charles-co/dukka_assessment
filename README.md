# Dukka Assessment

-  Decisions made;

    Frontend handles speech to text while backend just handles saving user details and authentication via auth token due to the following reasons stated;

    1. Real-time processing: Frontend speech-to-text conversion can provide real-time transcription as the user speaks, whereas backends may have a delay in processing the audio and returning the text.

    2. User experience: Frontend speech-to-text conversion can provide a better user experience, as it eliminates the need for the user to wait for a response from the server.

    3. Reduced server load and latency: By processing speech-to-text conversion on the frontend, the load on the server is reduced, which can improve the overall performance of the system.

    4. Offline support: Frontend speech-to-text conversion can work offline, as it does not rely on a network connection to the server.

    5. Privacy: Frontend speech-to-text conversion eliminates the need to send potentially sensitive audio data to the server, which can improve privacy for the user.

Tools Used: Docker (Backend), Python, Django & DRF, VueJS

Note: Code was tested Chrome Browser.


## Backend

Check [here](backend/README.md) on steps to run backend service.

## Frontend

Check [here](frontend/README.md) on steps to run frontend service separately.
