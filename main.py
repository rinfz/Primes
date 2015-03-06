import primes.utils.logger as logger
import primes.generator.prime as prime
import primes.generator.gaussian as gaussian


def main():
    primes = prime.Generator(maximum=2000)
    print primes.data
    primes.generate()
    primes.to_file()
    #gaussians = gaussian.Generator(minimum=complex(-100, -100), maximum=complex(100, 100))
    #gaussians.generate()
    #gaussians.to_file()


if __name__ == '__main__':
    logger.setup_logging()
    main()
