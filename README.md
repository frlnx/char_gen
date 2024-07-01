# Challenge Summary

I used pretty much 4 hours, as requested. It was an interesting challenge and I learned a few new tricks while hacking.

## Starting the project

`docker compose up --build`

You can now access the project at http://localhost:8008


## Architecture

I have chosen to use my preferred architecture, the hexagonal architecture. It may not be very visible in such a
small project, but it is there.

The service provider pattern is used to provide the services to the application. This way, the application is not
dependent on the implementation of the services, only on the interfaces. The services can also be moved a microservice
if needed, but in this case it is not necessary.

The provider pattern is used to decouple the application from the implementation of the services. This way, the
application does not care what implementation of the client the service is using. Running tests in this way is more
predictable and controllable. You also never need to worry about tests contacting OpenAI, which would be costful.

## Tests

No tests were implemented as per request.

If I were to implement tests, the service would be tested using the dummy client. The dummy client itself should then
be updated to give proper objects that behave like the real client. This way, the tests are not dependent on the real
client, and the tests can be run without contacting OpenAI.

For this small project, I would test the web application using pytest and requests. But were the project to grow,
I would use selenium to test the web application.

## Improvements

- Adding a CI/CD pipeline would be a good improvement. This way, the project can be tested and deployed automatically.
- Adding terraform for deployment, so the project can be deployed to AWS or GCP.
- Adding login and user management. This would require a Database, which I felt was out of scope for this project as
there was nothing requiring it.
- Using a proper frontend framework instead of barebone javascript. As I am ok with writing html and javascript, I
didn't focus on this.
- Streaming the response from OpenAI to the client. This would require a bit of work, but would make the application
feel more responsive.

## Features I wanted to make but shelved before even starting
 
- Generate character art using stable diffusion
- Use an uploaded picture as a basis for the text generation and character art

## Thank you

Thank you for reading this far. I hope you enjoyed the project. I am looking forward to your feedback.