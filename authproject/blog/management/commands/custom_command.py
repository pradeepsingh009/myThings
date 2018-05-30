from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):

    help = "this is a custom command"

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('poll_id', nargs='+', type=int,help="specify the poll id")

        # Named (optional) arguments
        parser.add_argument(
            '--delete',
            action='store_true',
            dest='delete',
            help='Delete poll instead of closing it',
        )

        # parser.add_argument("name",help="specifiy the name to be used")
        # parser.add_argument("age",help="specifiy the age to be used")


        # https://docs.python.org/3/library/argparse.html#name-or-flags
        #       parser.add_argument() arguments
        # name or flags - Either a name or a list of option strings, e.g. foo or -f, --foo.
        # action - The basic type of action to be taken when this argument is encountered at the command line.
        # nargs - The number of command-line arguments that should be consumed.
        # const - A constant value required by some action and nargs selections.
        # default - The value produced if the argument is absent from the command line.
        # type - The type to which the command-line argument should be converted.
        # choices - A container of the allowable values for the argument.
        # required - Whether or not the command-line option may be omitted (optionals only).
        # help - A brief description of what the argument does.
        # metavar - A name for the argument in usage messages.
        # dest - The name of the attribute to be added to the object returned by parse_args().



    def handle(self,*args,**kwargs):
        print(self)
        print("\n----------------------------")
        print(args)
        print("\n----------------------------")
        print(kwargs)

        self.stdout.write("Unterminated line", ending='')
        # https://docs.djangoproject.com/en/2.0/ref/django-admin/#extra-niceties
        self.stdout.write(self.style.ERROR("Unterminated line"))