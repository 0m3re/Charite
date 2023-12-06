<script lang="ts">
    // IMPORTS
    import { onMount } from 'svelte';
    import { sendMessage, sendAnnouncement, connectWebSocket, sendKill, closeWebSocket } from '../client/client';
    import { errorStore, responseStore } from '../client/client';

    // Function to connect WebSocket on component mount (Since main page on application startup)
    onMount(() => {
        console.log("Mounting component and connecting to WebSocket");
        connectWebSocket();
    });

    // Variables for form inputs
    let title = "";
    let body = "";
    let dateTime = "";
    let creator = "";
    let textFieldValue = "";

    // Function to Handle Announcements
    function handleSendAnnouncement() {
        console.log("Sending announcement");
        sendAnnouncement(title, body, dateTime, creator);
    }

    // Function to Handle Messages, restricting some commands (restricting just a test, maybe useful later)
    function handleSendMessage() {
        const restrictedCommands = ["kill", "create_announcement"];

        if (restrictedCommands.includes(textFieldValue.toLowerCase())) {
            console.log(`Command "${textFieldValue}" is restricted and cannot be sent.`);

            errorStore.set(`${textFieldValue} is not allowed.`);
            setTimeout(() => errorStore.set(""), 5000);
        } else {
            console.log("Sending command with text: ", textFieldValue.toLowerCase());
            sendMessage(textFieldValue.toLowerCase());
        }
    }

    function handleSendHello(){
        console.log("Sending Hello command");
        sendMessage("hello");
    }

    function handleSendKill() {
        console.log("Sending Kill command");
        sendKill();
    }

    function handleStartWebsocket(){
        console.log("Starting Websocket");
        connectWebSocket();
    }

    function handleCloseWebsocket(){
        console.log("Closing Websocket");
        closeWebSocket();
    }
</script>

<page>
    <actionBar title="Home" />
    <stackLayout>
        {#if $errorStore} <!-- Conditional Rendering, only display if exists-->
            <label class="error-label" text={`Error: ${$errorStore}`} />
        {/if}
        {#if $responseStore}
            <label class="response-label" text={`Response: ${$responseStore}`} />
        {/if}

        <button text="Send Hello" on:tap="{handleSendHello}" />
        <button text="Kill Server" on:tap="{handleSendKill}" />
        <button text="Open Websocket Connection" on:tap="{handleStartWebsocket}"/>
        <button text="Close Websocket Connection" on:tap="{handleCloseWebsocket}"/>

        <textField bind:text="{textFieldValue}" hint="Enter text..." />
        <button text="Send Message" on:tap="{handleSendMessage}" />

        <textField bind:text="{title}" hint="Title..." />
        <textField bind:text="{body}" hint="Body..." />
        <textField bind:text="{dateTime}" hint="Date and Time..." />
        <textField bind:text="{creator}" hint="Creator..." />
        <button text="Send Announcement" on:tap="{handleSendAnnouncement}" />
    </stackLayout>
</page>

<style>
    .error-label{
        font-size: large;
        color: red;
    }
    .response-label{
        font-size: large;
        color: blue;
    }
</style>