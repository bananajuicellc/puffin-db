# Vision

This document provides a roadmap for Puffin DB and describes some motivation for
the project.

## Overview

Store your structured data with history. The working copy is just a regular
SQLite3 database. History is available, syncable, and verifiable.

## Use cases

I want to be able to sync a database across devices with no unnecessary
conflicts.

I want to have backups that I am as confident in as I am a git db pushed to
GitHub and synced locally. (Either can be used to restore the other, no "one
true copy")

I want to be able to look at the history of the database and see how it changed
and why. (Recent history is more important than earlier versions, but it'd be
good to see full history sometimes)

I want to collaborate on a database and know who made which changes.

## Technical requirements

### Future-proof

The working copy of the database acts just like a normal SQLite database. The
other requirements ideally can be implemented without the need for triggers.

Why? SQLite aims to be incredibly stable. SQLite is a Recommended Storage
Format for datasets according to the US Library of Congress. Further
information:

* [SQLite, Version 3 (loc.gov)](https://www.loc.gov/preservation/digital/formats/fdd/fdd000461.shtml)
* [Recommended Formats Statement – Datasets
  (loc.gov)](https://www.loc.gov/preservation/resources/rfs/data.html)
* [LoC Recommended Storage Format (sqlite.org)](https://sqlite.org/locrsf.html)

Extensions for implementing the other requirements should aim to follow the same
transparency and self-documetation goals as SQLite itself.

### Synchronization

* Adding a row does not cause conflicts if I also add a row on another device.
* Updating a row does not cause conflicts if there was an update to the same
  row but a different column.
* Deleting a row does not cause conflicts if that row was not touched on other devices.
* It’s easy to create a Work-in-Progress branch that can be synced across
  devices without affecting the main / release branch.

### Commit history

* History storage is efficient.
* History storage allows for fast “diffs” across versions.
* I can verify who made which changes to the database.
* It is possible, but not nessarily efficient, to "change history", simlar to
  the rebase operation in git. Manual conflict resolution is expected to be
  necessary in this case.

## Related work

There are some options from the community for distributing structured data with
history. Rather than SQLite, these are mostly based on a JSON-like document /
key-value store.

* https://github.com/automerge/automerge
* https://github.com/hypercore-protocol/hyperdrive

I'm interested in data formats that can be useful for myself, family members,
researchers in the distant future. I'm a bit wary of technologies like automerge
and hyperdrive which have a custom data engine (though hyperdrive/Dat has a
local filesystem option for the working copy, which is nice for problems suited
to storing structured data in the filesystem).

[Perkeep](https://perkeep.org/) shares this goal, but I (Tim) find sharded blobs
difficult to work with (though they are JSON, so somewhat future-proof), and are
optimized for storing objects that don't change (such as photos or published
tweets).

