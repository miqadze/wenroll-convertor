<?php
if ($_SERVER['REQUEST_METHOD'] == 'GET' && isset($_GET['video_name'])) {
    $video_name = $_GET['video_name'];
    $bucket_name = "development-wenroll";
    $url = "https://s3.eu-central-1.amazonaws.com/$bucket_name/$video_name";
    $content = @file_get_contents($url);
    if ($content === false) {
        http_response_code(404);
        echo "Error: File not found";
    } else {
        file_put_contents($video_name, $content);
        http_response_code(200);
        echo "Process started";
        fastcgi_finish_request();
        exec("python3 convert.py $video_name 2>&1 >> py.log", $output);
    }
}
?>
