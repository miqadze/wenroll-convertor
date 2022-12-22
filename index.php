<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['video_name'])) {
    $video_name = $_POST['video_name'];
    $bucket_name = "test-wenroll";
    $url = "https://$bucket_name.s3.amazonaws.com/$video_name";
    $content = @file_get_contents($url);
    if ($content === false) {
        http_response_code(404);
        echo "Error: File not found";
    } else {
        file_put_contents($video_name, $content);
        http_response_code(200);
        echo "Process started";
        fastcgi_finish_request();
        //exec("python3 convert.py $video_name 2>&1 >> py.log", $output);
        exec("/bin/bash shell.sh $video_name 2>&1 >> py.log", $output);
    }
}
?>
