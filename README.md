### File_downloader

The service is designed to upload files to it and process them asynchronously <br>
with the possibility of later receiving a list of processed files.

<details>
<summary><strong>Coverage</strong></summary>

![Coverage](https://github.com/imwisagist/File_downloader/blob/main/infra/Coverage.png?raw=true)

</details>

<details>
<summary><strong>User capabilities</strong></summary>

#### What users can do
- Upload files to the server.
- Get a list of downloaded files.
- Asynchronously process files depending on the type.

</details>

<details>
<summary><strong>Launching in Docker containers</strong></summary>

- Cloning a remote repository.
- There is a .env file in the /infra directory, with environment variables, ready to use,
edit it at your discretion if required.
- Building and deploying containers.
```bash
git clone https://github.com/Imwisagist/File_downloader.git && cd File_downloader/infra && make build
``` 
- Uploading file endpoint [`http://localhost/api/v1/upload/`](http://localhost/api/v1/upload/)
<br> Choose the file and send POST request.
- Get file list endpoint [`http://localhost/api/v1/files/`](http://localhost/api/v1/files/)
<br> Send GET request to recieve a list of files.

</details>

<details>
<summary><strong>Suggestions about architecture</strong></summary>

### I suggest using the following methods:

1. Using Nginx as a load balancer.
2. Caching of requests.
3. Using Content Delivery Network.
4. Using a distributed database.
 
</details>

<details>
<summary><strong>Task</strong></summary>

![Task](https://github.com/imwisagist/File_downloader/blob/main/infra/Task.png?raw=true)

</details>
