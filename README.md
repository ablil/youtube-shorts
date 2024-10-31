# youtube-shorts

**Important**

**This is implmentation is not working on the cloud, it seems youtube is blocking all requests coming from aws IP addresses**

Restful API to download YouTube shorts.

```shell
curl http://{host}/youtube-shorts?url=https://www.youtube.com/shorts/5-KHxpgLMfU

# response 304
{
  "url": "direct download url"
}
```
