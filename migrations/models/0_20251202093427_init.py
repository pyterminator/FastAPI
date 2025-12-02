from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "username" VARCHAR(20) NOT NULL UNIQUE,
    "email" VARCHAR(50) NOT NULL UNIQUE,
    "password" VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS "todo" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "description" TEXT NOT NULL,
    "is_completed" INT NOT NULL DEFAULT 0,
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztmF1v2jAUhv9KxVUrdVPLmrXaHTC6dW1BonSqVFWRSQ7BqmOntrMWVfz32U5CEpMwkE"
    "ACrXfhfCTnPBz7dfLeCJkPRHweMp81vh28NygKQV2U7McHDRRFuVUbJBoREyiziJGQHHlS"
    "2caICFAmH4THcSQxo8pKY0K0kXkqENMgN8UUv8TgShaAnABXjscnZcbUhzcQ2c/o2R1jIH"
    "6pTOzrZxu7K6eRsV1ReWkC9dNGrsdIHNI8OJrKCaPzaEyltgZAgSMJ+vaSx7p8XV3aZdZR"
    "UmkekpRYyPFhjGIiC+2uyMBjVPNT1QjTYKCf8ql5enZ+dvHl69mFCjGVzC3ns6S9vPck0R"
    "DoDRsz40cSJREGY86tWNYCwCG81RC00iyUqgEbZQZuGcvMkMPMB2gzNJegGnYfhrroUIgX"
    "og29361B52drcHjbejgynmnquen3fmThTI16Mv+9zk2/bWgXplIoZmFEQENYwNtmjACiNT"
    "NqpVqIRyp3W4zXXbarQ273+zclyO0rm+L9bbs7ODw1xFUQllAc5BxtLIC7a636Qsa/l/5u"
    "zOsmVr/eMsfPlYtfE1kEeMk44IBew9RwvFIVIepBBbdUG+7T2+wev1k2A5k136A5ep3LSH"
    "E0VHuqKUjGrtO667S+dxsG4gh5z6+I+26JpvawJrMs89hFV9gMbQuiKDD96y50zUWwFWKc"
    "Aa8XY92Q+FDjfVNj/beZ6wV6nQni9dtalrMZHd46xRC9uQRoICca3ckSZJkGN0+OLJ1IPU"
    "3jKksDhAiTdRDOE/aRn7MKP6een7PAL0JCvDJesYbrERZz9uU0aM2h46wyiI5TP4naVyG4"
    "9eKRM9dvT6LiiJimXV4PgKCa47b1irZ7oOtkeLZN8WwBx96kSj5Tz1IBRXnMh4LukYL+Ue"
    "eeynfZ+q2rkPKf71xFEdBLYw2Iafh+Ajw9WUVDVVQtQOMrA1RPlJCswTLEX3f9XjXEQooF"
    "8p6qBh997MnjA4KFfNpNrEso6q6Xf1+xP6VoCkzIgJu7mBu015PXzcvL7C+9zsYz"
)
