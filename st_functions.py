import streamlit as st

def load_css():
    with open("style.css") as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

def st_button(icon, url, label, iconsize):
    if icon == 'twitter':
        button_code = f'''
        <p>
        <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
            <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-twitter" viewBox="0 0 16 16">
                <path d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334 0-.14 0-.282-.006-.422A6.685 6.685 0 0 0 16 3.542a6.658 6.658 0 0 1-1.889.518 3.301 3.301 0 0 0 1.447-1.817 6.533 6.533 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.325 9.325 0 0 1-6.767-3.429 3.289 3.289 0 0 0 1.018 4.382A3.323 3.323 0 0 1 .64 6.575v.045a3.288 3.288 0 0 0 2.632 3.218 3.203 3.203 0 0 1-.865.115 3.23 3.23 0 0 1-.614-.057 3.283 3.283 0 0 0 3.067 2.277A6.588 6.588 0 0 1 .78 13.58a6.32 6.32 0 0 1-.78-.045A9.344 9.344 0 0 0 5.026 15z"/>
            </svg>
            {label}
        </a>
        </p>'''
    elif icon == 'linkedin':
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-linkedin" viewBox="0 0 16 16">
                    <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
                </svg>
                {label}
            </a>
        </p>''' 
      
    elif icon == '':
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                {label}
            </a>
        </p>'''
        
    elif icon == 'codeforces':
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                 <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path fill="currentColor" d="M4.5 7.5A1.5 1.5 0 0 1 6 9v10.5A1.5 1.5 0 0 1 4.5 21h-3C.673 21 0 20.328 0 19.5V9c0-.828.673-1.5 1.5-1.5h3zm9-4.5A1.5 1.5 0 0 1 15 4.5v15a1.5 1.5 0 0 1-1.5 1.5h-3c-.827 0-1.5-.672-1.5-1.5v-15c0-.828.673-1.5 1.5-1.5h3zm9 7.5A1.5 1.5 0 0 1 24 12v7.5a1.5 1.5 0 0 1-1.5 1.5h-3a1.5 1.5 0 0 1-1.5-1.5V12a1.5 1.5 0 0 1 1.5-1.5h3z"/></svg>
                {label}
        </p>''' 
    
    elif icon == 'codechef':
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path fill="currentColor" d="M11.257.004c-.37.01-.735.04-1.1.095c-.54.054-1.08.325-1.675.595c-.757.324-1.515.649-2.218.703c-1.19.378-1.568.919-1.892 1.351c0 .054-.054.108-.054.108c-.433.865-.487 1.73-.325 2.595c.162.541.378 1.029.54 1.515c.38 1.028.758 2 .92 3.136c.163.325.324.757.432 1.19c.27.865.542 1.838 1.353 2.595l.006-.003c.017.019.03.04.048.057l.021-.01l-.02-.584c.648-.974 1.566-1.623 2.864-1.893c.52-.11 1.081-.15 1.663-.128a8.773 8.773 0 0 1 1.798.236c1.46.378 2.595 1.136 2.65 1.785c.027.354.04.695.032 1.036c0 .064-.004.128-.007.193l.136.068a.639.639 0 0 0 .206-.19l.003-.003l.006-.008c.04-.054.075-.124.11-.194c.02-.037.038-.086.056-.129c.205-.462.362-1.153.538-1.963c.054-.27.11-.487.163-.703c.433-.973 1.027-1.838 1.622-2.65c.973-1.35 1.892-2.595 1.784-4.055c-1.784-3.461-4.272-4.002-5.57-4.272c-.216-.054-.323-.054-.485-.108c-1.338-.244-2.494-.396-3.605-.365zM16.3 14.383a9.86 9.86 0 0 0-.032-.983c-.054-.703-1.19-1.46-2.704-1.838a9.536 9.536 0 0 0-1.744-.236a6.761 6.761 0 0 0-1.555.128c-1.244.27-2.216.92-2.811 1.892l.051 1.431c.667-.355 1.733-.874 3.14-1c.065-.005.136-.005.204-.009c.117-.013.266-.044.444-.044c1.607 0 3.268.534 4.877 1.648c.039-.274.06-.549.07-.823l.045.023c.002-.063.014-.127.015-.19zM11.256.058c.124-.004.254.01.379.011c-.23-.002-.459.003-.687.016c.103-.006.205-.024.308-.027zm.498.015zM10.44.13c-.076.009-.153.013-.229.024c-.817.117-1.774.701-2.75 1.045c.355-.132.714-.296 1.075-.45c.54-.27 1.135-.541 1.621-.595c.094-.014.189-.013.283-.024zm-.229.24c.162 0 .379 0 .541.054a.995.995 0 0 0-.37-.014a1.174 1.174 0 0 1 .316.068c.58 1-.426 5.279-.679 8.149a57.37 57.37 0 0 0 .463 2.72c-.703-1.784-1.406-4.921-1.515-7.354c-.054-.973.001-1.839.218-2.487C9.4.855 9.725.423 10.21.369zm3.136.27c-.81 2.11-.918 6.11-.972 7.354c-.054.54 0 1.73.054 2.595c0 .216.054.432.054.649c0-.217-.054-.379-.054-.595c-.433-3.244-.974-7.136.918-10.002zm3.352.379c-.27 2.162-1.405 3.19-1.783 5.3c-.108 1.676-.325 3.622-.379 5.298c-.054-1.676 0-3.46.27-5.245c.27-1.838.865-3.677 1.892-5.353zM6.32 1.45zm.21.197a.856.856 0 0 1 .6.236l-.014-.007c.133.092.266.209.393.384c-.204.968.255 3.032.04 4.67c.076 1.548.071 3.18.849 4.459c-.98-1.51-1.176-3.438-1.322-5.236c-.113-1.09-.204-2.097-.464-2.903c-.144-.305-.269-.575-.384-.822c-.024-.037-.044-.079-.07-.114a.582.582 0 0 1-.162-.377c0-.054.053-.162.108-.162c.054-.054.161-.056.215-.11a1.013 1.013 0 0 1 .21-.018zm-1.347.613c-.06.02-.092.041-.14.061c.177-.034.362.034.52.318c-.188.892.436 3.369.428 5.104c.313 1.848.55 3.85 1.572 5.115c-1.19-1.351-1.676-3.73-2.054-5.731c-.325-1.568-.596-2.92-1.136-3.352c-.054-.108-.108-.163-.108-.271c0-.162 0-.379.108-.595c-.277.634-.405 1.267-.37 1.901a3.844 3.844 0 0 1 .37-1.901c0-.054.054-.054.054-.108c.012-.016.031-.035.044-.051a.878.878 0 0 1 .226-.257c.055-.061.096-.12.159-.182c-.053.056-.088.11-.134.165c.027-.018.052-.037.084-.052a.49.49 0 0 1 .377-.164zm-.377.164c-.004.007-.008.01-.012.018l.037-.03l-.025.012zm14.76 1.134l-.005.015c.038-.005.075-.017.113-.015c-.037-.002-.076.01-.115.02c-.863 2.642-1.887 5.284-2.911 7.926a.018.018 0 0 1-.002.003c-.087.465-.234.884-.54 1.19c.433-.487.486-1.191.54-2.056c.054-.811.054-1.676.487-2.542c0-.053.001-.105.053-.159l.001-.002c.097-.353.202-.689.317-1.018c.418-1.29 1.14-3.166 2.013-3.34c.016-.006.034-.019.05-.022zM8.374 16.21l-.324.108c.162.217.27.38.378.433a.784.784 0 0 0 .379.108c.054 0 .161 0 .215-.054l.812-.27c.054 0 .108-.054.162-.054c.108 0 .162 0 .27.054l.271.27l.27-.054c-.108-.162-.27-.323-.378-.377c-.108-.054-.217-.11-.379-.11h-.108l-.866.325h-.161c-.109 0-.216 0-.27-.054c-.054-.054-.163-.162-.271-.325zm-2.596.541c-.27.162-.649.433-1.19.649c-.54.216-.973.433-1.19.649c-.215.216-.323.432-.323.649c0 .108.054.163.162.217c.054.054.163.054.217.108a27.9 27.9 0 0 1 2.216 1.08c.109.054.217.163.272.217c.054.054.107.054.161.054c.109 0 .27-.053.378-.162c.108-.108.163-.217.163-.325c0-.108-.055-.161-.163-.215c0 0-.433-.217-1.19-.541a11.967 11.967 0 0 1-1.188-.595c.162-.27.486-.487.973-.703c.54-.216.92-.433 1.081-.595c.054-.054.054-.108.054-.162a.412.412 0 0 0-.108-.217a.415.415 0 0 0-.27-.108zm11.247 0a.408.408 0 0 0-.216.108c-.054.108-.109.163-.109.217v.054c.162.162.38.27.704.378c.27.054.54.163.811.217c.324.108.54.27.649.486v.055c0 .054-.109.162-.325.27c-.108.054-.325.217-.595.433c-.27.162-.433.323-.595.377c-.216.109-.378.217-.432.326c-.054.054-.054.107-.054.161c0 .108.054.108.108.216s.162.11.216.11c.054 0 .108-.056.162-.056c.27-.162.65-.378 1.082-.757c.486-.378.865-.648 1.082-.81c.216-.108.323-.217.323-.38c0-.053 0-.161-.108-.215c-.378-.433-.918-.702-1.567-.919c-.108-.054-.27-.109-.595-.163c-.162-.054-.325-.108-.433-.108zm-2.974.81c-.27 0-.487.056-.649.218c-.216.162-.27.432-.216.757c0 .27.108.486.27.703c.162.216.379.325.595.325c.162 0 .27-.056.433-.11c.27-.162.379-.432.379-.918c0-.379-.109-.649-.271-.81a.915.915 0 0 0-.541-.164zm-4.488.055c-.27 0-.486.055-.648.217c-.217.162-.27.432-.216.757c0 .27.107.486.27.702s.378.326.594.326c.163 0 .271-.056.433-.11c.27-.162.378-.432.378-.918c0-.433-.108-.703-.27-.81a.915.915 0 0 0-.54-.164zm0 .65c.163 0 .271.108.271.27c0 .162-.163.27-.27.27c-.163 0-.27-.108-.27-.27s.107-.27.27-.27zm4.38.054c.162 0 .271.107.271.27c0 .108-.109.27-.27.27c-.163 0-.27-.108-.27-.27c0-.163.107-.27.27-.27zm-2.703 2.108l.162.324a.947.947 0 0 0 .216.271c.054.054.163.162.27.162h.109c.108 0 .161 0 .215-.054c.054-.054.164-.054.218-.108l.161-.162c.054-.054.108-.109.108-.163c.054-.054.054-.108.108-.162c0-.054.054-.108.054-.108c-.054.108-.162.216-.216.324c-.108.054-.161.163-.27.163c-.107.054-.216.054-.324.054s-.216 0-.27-.054c-.108 0-.163-.054-.217-.108l-.162-.163c-.054-.054-.108-.162-.162-.216zm-.866 1.028c-1.136 0-1.838 1.514-3.46.162c-.432 2.65 2.758 2.866 4.11 1.73c.92-.81.648-1.946-.65-1.892zm2.866 0c-1.297-.054-1.568 1.082-.648 1.893c1.351 1.135 4.54.918 4.108-1.731c-1.622 1.352-2.27-.162-3.46-.162z"/></svg>
                {label}
        </p>'''
    
    elif icon=='leetcode':
         button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-code-square" viewBox="0 0 16 16">
                  <path d="M10.478 1.647a.5.5 0 1 0-.956-.294l-4 13a.5.5 0 0 0 .956.294l4-13zM4.854 4.146a.5.5 0 0 1 0 .708L1.707 8l3.147 3.146a.5.5 0 0 1-.708.708l-3.5-3.5a.5.5 0 0 1 0-.708l3.5-3.5a.5.5 0 0 1 .708 0zm6.292 0a.5.5 0 0 0 0 .708L14.293 8l-3.147 3.146a.5.5 0 0 0 .708.708l3.5-3.5a.5.5 0 0 0 0-.708l-3.5-3.5a.5.5 0 0 0-.708 0z"/>
                  </svg>
                {label}
        </p>'''
       
    return st.markdown(button_code, unsafe_allow_html=True)
