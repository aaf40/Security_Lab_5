from dh import dh_generatePublicKey, dh_generateSecretKey

def main():
    # Initialize the parameters
    P = 23  # Prime number
    G = 9   # Generator
    x = 0   # Alice's public key
    a = 4   # Alice's private key
    y = 0   # Bob's public key
    b = 3   # Bob's private key
    ka = 0  # Alice's secret key
    kb = 0  # Bob's secret key

    # Display the agreed-upon public parameters
    print("The value of P:", P)
    print("The value of G:", G)

    # Generate and display Alice's private key
    print("The private key a for Alice:", a)
    x = dh_generatePublicKey(P, G, a)

    # Generate and display Bob's private key
    print("The private key b for Bob:", b)
    y = dh_generatePublicKey(P, G, b)

    # Each computes their secret key using the other's public key
    ka = dh_generateSecretKey(y, a, P)
    kb = dh_generateSecretKey(x, b, P)

    # Display the secret keys calculated by Alice and Bob
    print("Secret key for Alice is:", ka)
    print("Secret Key for Bob is:", kb)

    # Verify that the shared secrets match
    assert ka == kb, "The secret keys do not match!"

if __name__ == '__main__':
    main()
