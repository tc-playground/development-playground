# JWT - JSON Web Token

---

## Introduction

* A `jwt` token is a method for allowing __stateless authentication__, without actually storing any information about the user on the system itself.

    > NB: Aas opposed to __session based authentication).

* `jwt` acts as a way to authorize users in a secure manner, without actually storing any information (except for a `secret-key`) on the application server.

* `jwt` is a compact URL-safe means of representing `claims` to be transferred between two `parties`.

* `jwt`  token is simply a JSON object that is signed by its author. this tells you exactly two things about the data:

    1. The author of the token was in the possession of the signing secret.
    
    2. The data has not been modified since it was signed.

    > NB: It's important to know that `JWT` does not provide encryption of the payload.

---

## Overview


* A `jwt` consists of three parts separated by a `.`:

    * The `header` specifies the `signing method` _one-way hashing algorithm_ and other details used to generate the `signature`. 

    * The `claims` (`payload`) that contains application specific information e.g. 'username', and _token expiry_ information.

        * `iss`: The `issuer` of the claim that denotes the application making the call.

        * `iat`: The `issue at time` contains the `UTC Unix time` at which this token was issued.

        * `sub`: The `subject` of this token, e.g. is the user associated with the relevant action,

    * The `signature` that is created by hashing the `header` and `payload` along with a secret `key`.

* A `jwt` token's `header` and `payload` are NOT encrypted. They are Base64 encoded.

* The __application__ that issues the `jwt` will have a `secret key` known only to itself to decode the token. 

    * The

* A `jwt` token is verified by generating a new `signature` from the `header`, `payload`, and, `secret key` and checking it matches the one in the token.


> NB: `jwt` tokens are often used in `OAuth` based security implementations.

---

## Signing Methods

* __Symmetric__

    * The `HMAC` signing method (HS256,HS384,HS512) expects `[]byte values` for signing and validation.

    * Symmetric signing methods, such as `HSA`, use only a single secret.

    * Symmetric signing methods work the best when both producers and consumers of tokens are trusted, or even the same system. 
    
    * Since the same secret is used to both sign and validate tokens, you can't easily distribute the key for validation.

* __Asymmetric__

    * The `RSA` signing method (RS256,RS384,RS512) expects `*rsa.PrivateKey` for signing and `*rsa.PublicKey` for validation.

    * The `ECDSA` signing method (ES256,ES384,ES512) expects `*ecdsa.PrivateKey` for signing and *`ecdsa.PublicKey` for validation.

    * Asymmetric signing methods, such as `RSA`, `ECDSA` use different keys for signing and verifying tokens.

    * This makes it possible to produce tokens with a private key, and allow any consumer to access the public key for verification.

---

## Advantages of Token based Authentication


* __Cross-domain / CORS__ : cookies + CORS don’t play well across different domains. A token-based approach allows you to make AJAX calls to any server, on any domain because you use an HTTP header to transmit the user information.

* __Stateless__: there is no need to keep a session store, the token is a self-contained entity that conveys all the user information.

* __CDN__: you can serve all the assets of your app from a CDN (e.g. javascript, HTML, images, etc.), and your server side is just the API.

* __Decoupling__: you are not tied to a particular authentication scheme. The token might be generated anywhere, hence your API can be called from anywhere with a single way of authenticating those calls.

* __Mobile ready__: when you start working on a native platform (iOS, Android, Windows 8, etc.) cookies are not ideal when consuming a secure API (you have to deal with cookie containers). Adopting a token-based approach simplifies this a lot.

* __CRSF__: since you are not relying on cookies, you don’t need to protect against cross site requests.

---

## References

* [jwt.io](https://jwt.io/) - Home and decoder tool.

* __Golang__

    * [jwt-go](https://github.com/dgrijalva/jwt-go) - JWT implementation.
    * [jwt-docs](https://godoc.org/github.com/dgrijalva/jwt-go) - `jwt-go` API docs.
    * [JWT Auth Tutorial](https://www.sohamkamani.com/blog/golang/2019-01-01-jwt-authentication)
    * [JWT Auth Tutorial](https://auth0.com/blog/authentication-in-golang)
    * [JWT Auth Tutorial](https://medium.com/@raul_11817/securing-golang-api-using-json-web-token-jwt-2dc363792a48)
    * [JWT Auth Tutorial](https://tutorialedge.net/golang/authenticating-golang-rest-api-with-jwts)
    * [JWT Auth Tutorial](https://www.thepolyglotdeveloper.com/2017/03/authenticate-a-golang-api-with-json-web-tokens)


