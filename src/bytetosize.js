function bytesToSize(bytes) {
    const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB', "PB", "EB", "ZB", "YB"];

    if (bytes === 0) {
        return 'n/a';
    }

    const i = Math.floor(Math.log(Math.abs(bytes)) / Math.log(1024));

    if (i === 0) {
        return `${bytes} ${sizes[i]}`;
    }

    return `${(bytes / (1024 ** i)).toFixed(1)} ${sizes[i]}`;
}