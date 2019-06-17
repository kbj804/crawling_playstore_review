function parse_reviews() {
    const commentContEle = document.querySelector('div[jsname="fk8dgd"]');
    if (!commentContEle || !commentContEle.firstChild) {
        throw new Error('CONT_NOT_EXIST');
    }

    // Regular expressions
    const regexToExtract = new RegExp(/^\w*;_;\$(\d+) \w*;_;\$\d+$/);
    const regexToReplace = new RegExp(/^(\w*;_;\$)\d+( \w*;_;\$\d+)$/);

    // Commnet list.
    const comments = [];

    const firstJsData = commentContEle.firstElementChild.getAttribute('jsdata');

    let jsDataIndex = firstJsData.match(regexToExtract)[1];
    while (true) {
        const jsDataAttr = firstJsData.replace(regexToReplace, (_, a, b) => `${a}${jsDataIndex}${b}`);
        const commentEle = document.querySelector(`div[jsdata="${jsDataAttr}"]`);
        if (commentEle) {
            comments.push(commentEle.querySelector(`span[jsname="bN97Pc"]`).textContent);
            commentEle.remove();
            jsDataIndex++;
        } else {
            break;
        }
    }

    return JSON.stringify(comments);
}